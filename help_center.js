//document.addEventListener("DOMContentLoaded", () => {
//
//    gsap.registerPlugin(ScrollTrigger);
//
//
//    /* ======================================
//       HERO ANIMATION
//    ====================================== */
//
//    const heroTimeline = gsap.timeline();
//
//    heroTimeline
//
//        .from(".help-logo", {
//            y: -25,
//            opacity: 0,
//            duration: 0.6
//        })
//
//        .from(".support-btn", {
//            x: 30,
//            opacity: 0,
//            duration: 0.5
//        }, "-=0.3")
//
//        .from(".help-hero-content > *", {
//            y: 40,
//            opacity: 0,
//            duration: 0.7,
//            stagger: 0.15,
//            ease: "power3.out"
//        });
//
//
//    /* ======================================
//       SUPPORT CARDS
//    ====================================== */
//
//    gsap.from(".support-card", {
//
//        scrollTrigger: {
//            trigger: ".support-section",
//            start: "top 82%"
//        },
//
//        y: 70,
//        opacity: 0,
//        duration: 0.7,
//        stagger: 0.15,
//        ease: "power3.out"
//
//    });
//
//
//    /* ======================================
//       FAQ ANIMATION
//    ====================================== */
//
//    gsap.from(".faq-item", {
//
//        scrollTrigger: {
//            trigger: ".faq-list",
//            start: "top 80%"
//        },
//
//        x: -50,
//        opacity: 0,
//        duration: 0.6,
//        stagger: 0.1,
//        ease: "power2.out"
//
//    });
//
//
//    /* ======================================
//       CONTACT ANIMATION
//    ====================================== */
//
//    gsap.from(".contact-box", {
//
//        scrollTrigger: {
//            trigger: ".contact-box",
//            start: "top 82%"
//        },
//
//        y: 60,
//        opacity: 0,
//        scale: 0.96,
//        duration: 0.8,
//        ease: "power3.out"
//
//    });
//
//
//    /* ======================================
//       EMERGENCY ANIMATION
//    ====================================== */
//
//    gsap.from(".emergency-box", {
//
//        scrollTrigger: {
//            trigger: ".emergency-box",
//            start: "top 85%"
//        },
//
//        x: -80,
//        opacity: 0,
//        duration: 0.8,
//        ease: "power3.out"
//
//    });
//
//
//    /* ======================================
//       FAQ ACCORDION
//    ====================================== */
//
//    const faqQuestions =
//        document.querySelectorAll(".faq-question");
//
//
//    faqQuestions.forEach(question => {
//
//        question.addEventListener("click", () => {
//
//            const currentItem =
//                question.parentElement;
//
//            const currentAnswer =
//                currentItem.querySelector(".faq-answer");
//
//
//            document
//                .querySelectorAll(".faq-item")
//                .forEach(item => {
//
//                    if (item !== currentItem) {
//
//                        item.classList.remove("active");
//
//                        const answer =
//                            item.querySelector(".faq-answer");
//
//                        answer.style.maxHeight = null;
//
//                    }
//
//                });
//
//
//            currentItem.classList.toggle("active");
//
//
//            if (currentItem.classList.contains("active")) {
//
//                currentAnswer.style.maxHeight =
//                    currentAnswer.scrollHeight + "px";
//
//            } else {
//
//                currentAnswer.style.maxHeight = null;
//
//            }
//
//        });
//
//    });
//
//
//    /* ======================================
//       SEARCH
//    ====================================== */
//
//    const searchInput =
//        document.getElementById("helpSearch");
//
//    const searchButton =
//        document.getElementById("searchBtn");
//
//    const faqItems =
//        document.querySelectorAll(".faq-item");
//
//    const noResult =
//        document.getElementById("noResult");
//
//
//    function searchFAQ() {
//
//        const searchText =
//            searchInput.value
//                .toLowerCase()
//                .trim();
//
//        let found = false;
//
//
//        faqItems.forEach(item => {
//
//            const question =
//                item.dataset.question.toLowerCase();
//
//
//            if (
//                searchText === "" ||
//                question.includes(searchText)
//            ) {
//
//                item.style.display = "block";
//
//                found = true;
//
//            } else {
//
//                item.style.display = "none";
//
//            }
//
//        });
//
//
//        noResult.style.display =
//            found ? "none" : "block";
//
//
//        if (searchText !== "" && found) {
//
//            gsap.fromTo(
//                ".faq-item[style='display: block;']",
//                {
//                    opacity: 0,
//                    y: 15
//                },
//                {
//                    opacity: 1,
//                    y: 0,
//                    duration: 0.4,
//                    stagger: 0.05
//                }
//            );
//
//        }
//
//    }
//
//
//    searchButton.addEventListener(
//        "click",
//        searchFAQ
//    );
//
//
//    searchInput.addEventListener(
//        "input",
//        searchFAQ
//    );
//
//
//    searchInput.addEventListener(
//        "keydown",
//        event => {
//
//            if (event.key === "Enter") {
//
//                searchFAQ();
//
//            }
//
//        }
//    );
//
//
//    /* ======================================
//       SUPPORT BUTTON HOVER
//    ====================================== */
//
//    document
//        .querySelectorAll(
//            ".support-btn, .contact-btn, .emergency-btn"
//        )
//        .forEach(button => {
//
//            button.addEventListener(
//                "mouseenter",
//                () => {
//
//                    gsap.to(button, {
//                        y: -3,
//                        scale: 1.03,
//                        duration: 0.25
//                    });
//
//                }
//            );
//
//
//            button.addEventListener(
//                "mouseleave",
//                () => {
//
//                    gsap.to(button, {
//                        y: 0,
//                        scale: 1,
//                        duration: 0.25
//                    });
//
//                }
//            );
//
//        });
//
//
//    /* ======================================
//       SCROLL REFRESH
//    ====================================== */
//
//    window.addEventListener(
//        "load",
//        () => {
//            ScrollTrigger.refresh();
//        }
//    );
//
//});