// ================= SIDEBAR =================

const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");

menuBtn.addEventListener("click", () => {
    sidebar.classList.toggle("show");
});


// ================= MODAL =================

const modal = document.getElementById("testModal");
const addTestBtn = document.getElementById("addTestBtn");
const closeModal = document.getElementById("closeModal");
const cancelBtn = document.getElementById("cancelBtn");

addTestBtn.addEventListener("click", () => {
    modal.classList.add("show");
});

closeModal.addEventListener("click", () => {
    modal.classList.remove("show");
});

cancelBtn.addEventListener("click", () => {
    modal.classList.remove("show");
});


// Modal outside click

modal.addEventListener("click", (event) => {

    if (event.target === modal) {
        modal.classList.remove("show");
    }

});


// ================= SEARCH =================

const testSearch = document.getElementById("testSearch");
const categoryFilter = document.getElementById("categoryFilter");
const statusFilter = document.getElementById("statusFilter");
const rows = document.querySelectorAll("#testTable tr");

function filterTests() {

    const searchValue = testSearch.value.toLowerCase();
    const categoryValue = categoryFilter.value;
    const statusValue = statusFilter.value;

    let visibleCount = 0;

    rows.forEach(row => {

        const text = row.innerText.toLowerCase();

        const category = row.dataset.category;
        const status = row.dataset.status;

        const searchMatch =
            text.includes(searchValue);

        const categoryMatch =
            categoryValue === "all" ||
            category === categoryValue;

        const statusMatch =
            statusValue === "all" ||
            status === statusValue;

        if (
            searchMatch &&
            categoryMatch &&
            statusMatch
        ) {

            row.style.display = "";
            visibleCount++;

        } else {

            row.style.display = "none";

        }

    });

    document.getElementById("entryText").innerText =
        `Showing ${visibleCount} entries`;

}


// Search event

testSearch.addEventListener(
    "input",
    filterTests
);


// Category filter

categoryFilter.addEventListener(
    "change",
    filterTests
);


// Status filter

statusFilter.addEventListener(
    "change",
    filterTests
);


// Filter button

document.getElementById("filterBtn")
    .addEventListener("click", filterTests);


// ================= FORM =================

const testForm = document.getElementById("testForm");

testForm.addEventListener("submit", function(event) {

    event.preventDefault();

    alert("Lab Test added successfully!");

    testForm.reset();

    modal.classList.remove("show");

});


// ================= DELETE =================

document.querySelectorAll(".delete")
    .forEach(button => {

        button.addEventListener("click", function() {

            const row = this.closest("tr");

            const testName =
                row.querySelector("strong").innerText;

            const confirmDelete =
                confirm(
                    `Are you sure you want to delete "${testName}"?`
                );

            if (confirmDelete) {

                row.remove();

                alert("Test deleted successfully!");

            }

        });

    });


// ================= VIEW =================

document.querySelectorAll(".view")
    .forEach(button => {

        button.addEventListener("click", function() {

            const row = this.closest("tr");

            const testName =
                row.querySelector("strong").innerText;

            alert(
                `Viewing Lab Test:\n\n${testName}`
            );

        });

    });


// ================= EDIT =================

document.querySelectorAll(".edit")
    .forEach(button => {

        button.addEventListener("click", function() {

            const row = this.closest("tr");

            const testName =
                row.querySelector("strong").innerText;

            alert(
                `Edit Lab Test:\n\n${testName}`
            );

        });

    });