let editRestaurantId = null;

function startEdit(restaurant) {
    editRestaurantId = restaurant.id;

    document.getElementById('formTitle').innerText = `Редагувати ресторан "${restaurant.title}"`;
    document.querySelector('#restaurantForm button[type="submit"]').innerText = 'Зберегти зміни';

    document.getElementById('title').value = restaurant.title;
    document.getElementById('address').value = restaurant.address;
    document.getElementById('website').value = restaurant.website;
    document.getElementById('phone').value = restaurant.phone;

    const specSelect = document.getElementById('specializations');
    Array.from(specSelect.options).forEach(option => {
        option.selected = restaurant.specs.includes(option.value);
    });

    document.getElementById('restaurantForm').scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('restaurantForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('title', document.getElementById('title').value);
    formData.append('address', document.getElementById('address').value);
    formData.append('website', document.getElementById('website').value);
    formData.append('phone', document.getElementById('phone').value);

    const specSelect = document.getElementById('specializations');
    Array.from(specSelect.selectedOptions).forEach(option => {
        formData.append('specializations', option.value);
    });

    const imageInput = document.getElementById('image');
    if (imageInput.files[0]) {
        formData.append('image', imageInput.files[0]);
    }

    let url = '';
    if (editRestaurantId) {
        url = `/restaurant/edit/${editRestaurantId}/`;
    }

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Помилка: ' + data.error);
        } else {
            alert(editRestaurantId ? 'Дані успішно оновлено!' : 'Ресторан успішно додано!');
            window.location.reload();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Сталася помилка при відправці');
    });
});

function deleteRestaurant(restaurantId) {
    if (confirm('Ви впевнені, що хочете видалити цей ресторан?')) {
        fetch(`/restaurant/delete/${restaurantId}/`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Помилка: ' + data.error);
            } else {
                alert(data.message);
                window.location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Сталася помилка при видаленні');
        });
    }
}