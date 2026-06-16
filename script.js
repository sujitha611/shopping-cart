const cartList = document.getElementById("cartList");
const totalPriceEl = document.getElementById("totalPrice");

let cart = [];
let total = 0;

// Add item
function addToCart(name, price) {
  cart.push({ name, price });
  total += price;
  updateCart();
}

// Remove item
function removeItem(index) {
  total -= cart[index].price;
  cart.splice(index, 1);
  updateCart();
}

// Update cart UI
function updateCart() {
  cartList.innerHTML = "";

  cart.forEach((item, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      ${item.name} - ₹${item.price}
      <button class="remove" onclick="removeItem(${index})">Remove</button>
    `;
    cartList.appendChild(li);
  });

  totalPriceEl.innerText = total;
}
