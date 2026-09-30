/* ================= MOBILE MENU ================= */

const menuBtn = document.getElementById("menuBtn");
const navbar = document.getElementById("navbar");

menuBtn.addEventListener("click", () => {

    navbar.classList.toggle("active");

    const icon = menuBtn.querySelector("i");

    if (navbar.classList.contains("active")) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-xmark");
    } else {
        icon.classList.remove("fa-xmark");
        icon.classList.add("fa-bars");
    }

});


/* Close menu after clicking link */

document.querySelectorAll(".navbar a").forEach(link => {

    link.addEventListener("click", () => {
        navbar.classList.remove("active");

        const icon = menuBtn.querySelector("i");

        icon.classList.remove("fa-xmark");
        icon.classList.add("fa-bars");
    });

});


/* ================= SCROLL REVEAL ================= */

const revealElements = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver(
    (entries, observer) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.classList.add("show");

                observer.unobserve(entry.target);

            }

        });

    },
    {
        threshold: 0.15
    }
);

revealElements.forEach(element => {
    revealObserver.observe(element);
});


/* ================= COUNTER ================= */

const counters = document.querySelectorAll(".counter");

let counterStarted = false;

const statsSection = document.querySelector(".stats");

const counterObserver = new IntersectionObserver(
    (entries) => {

        if (entries[0].isIntersecting && !counterStarted) {

            counterStarted = true;

            counters.forEach(counter => {

                const target = Number(counter.dataset.target);

                let current = 0;

                const increment = target / 100;

                const updateCounter = () => {

                    current += increment;

                    if (current < target) {

                        counter.textContent =
                            Math.floor(current).toLocaleString();

                        requestAnimationFrame(updateCounter);

                    } else {

                        counter.textContent =
                            target.toLocaleString() + "+";

                    }

                };

                updateCounter();

            });

        }

    },
    {
        threshold: 0.3
    }
);

counterObserver.observe(statsSection);


/* ================= HEADER SHADOW ================= */

window.addEventListener("scroll", () => {

    const header = document.querySelector(".header");

    if (window.scrollY > 50) {
        header.style.boxShadow =
            "0 5px 25px rgba(0,0,0,.10)";
    } else {
        header.style.boxShadow =
            "0 3px 20px rgba(0,0,0,.06)";
    }

});