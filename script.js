async function loadBicycles() {
    const response = await fetch("/bicycles");
    const bicycles = await response.json();

    const container = document.getElementById("bicycles");
    container.innerHTML = "";

    for (const bicycle of bicycles) {
        container.innerHTML += `
            <div class="bike-card">
                <h3>${bicycle.brand}</h3>
                <p>Тип: ${bicycle.type}</p>
                <p>Цена: ${bicycle.price}</p>
                <p>Статус: ${bicycle.status}</p>

                ${
                    bicycle.status === "available"
                    ? `<button onclick="rentBicycle(${bicycle.id})">Арендовать</button>`
                    : `<button onclick="returnBicycle(${bicycle.id})">Вернуть</button>`
                }
            </div>
        `;
    }
}


async function rentBicycle(id) {
    const userId = document.getElementById("user-select").value;

    const response = await fetch(
    `/bicycles/${id}/rent?user_id=${userId}`,
    {
        method: "POST"
    }
    );

    if (response.ok) {
        alert("Велосипед успешно арендован");
    } else {
        const error = await response.json();
        alert(error.detail);
    }

    loadBicycles();
    loadRentals();
}


async function returnBicycle(id) {
    const response = await fetch(
    `/bicycles/${id}/return`,
    {
        method: "POST"
    }
    );

    if (response.ok) {
        alert("Велосипед успешно возвращён");
    } else {
        const error = await response.json();
        alert(error.detail);
    }

    loadBicycles();
    loadRentals();
}


async function loadRentals() {
    const response = await fetch("/rentals");
    const rentals = await response.json();

    const container = document.getElementById("rentals");
    container.innerHTML = "";

    for (const rental of rentals) {
        container.innerHTML += `
            <div class="rental-card">
                <p><strong>Пользователь:</strong> ${
                    rental.user === null
                    ? "Не указан"
                    : rental.user
                }</p>

                <p><strong>Велосипед:</strong> ${rental.bicycle}</p>

                <p><strong>Начало аренды:</strong> ${rental.rented_at}</p>

                <p><strong>Возврат:</strong> ${
                    rental.returned_at === null
                    ? "Ещё не возвращён"
                    : rental.returned_at
                }</p>
            </div>
        `;
    }
}


async function loadUsers() {
    const response = await fetch("/users");
    const users = await response.json();

    const select = document.getElementById("user-select");
    select.innerHTML = "";

    for (const user of users) {
        select.innerHTML += `
            <option value="${user.id}">
                ${user.name}
            </option>
        `;
    }
}


loadBicycles();
loadRentals();
loadUsers();
