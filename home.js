document.addEventListener("DOMContentLoaded", () => {

    // GSAP plugin register
    gsap.registerPlugin(ScrollTrigger);


    /* ==========================================
       PAGE LOAD ANIMATION
    ========================================== */

    const pageTimeline = gsap.timeline();

    pageTimeline
        .from(".logo", {
            y: -30,
            opacity: 0,
            duration: 0.7
        })

        .from(".nav-menu li", {
            y: -20,
            opacity: 0,
            duration: 0.5,
            stagger: 0.1
        }, "-=0.4")

        .from(".support-number", {
            x: 30,
            opacity: 0,
            duration: 0.5
        }, "-=0.3")

        .from(".appointment-btn", {
            scale: 0.8,
            opacity: 0,
            duration: 0.5
        }, "-=0.3");


    /* ==========================================
       HERO ANIMATION
    ========================================== */

    const heroTimeline = gsap.timeline({
        delay: 0.3
    });

    heroTimeline

        .from(".hero-tag", {
            x: -70,
            opacity: 0,
            duration: 0.8
        })

        .from(".hero-title", {
            x: -80,
            opacity: 0,
            duration: 0.9
        }, "-=0.4")

        .from(".hero-text", {
            x: -50,
            opacity: 0,
            duration: 0.7
        }, "-=0.5")

        .from(".hero-buttons", {
            y: 30,
            opacity: 0,
            duration: 0.7
        }, "-=0.4")

        .from(".trust-area", {
            y: 30,
            opacity: 0,
            duration: 0.6
        }, "-=0.4")

        .from(".hero-image", {
            scale: 1.15,
            opacity: 0,
            duration: 1.2,
            ease: "power3.out"
        }, "-=1");



    /* ==========================================
       HERO FLOATING CARDS
    ========================================== */

    gsap.from(".floating-card", {

        y: 40,

        opacity: 0,

        duration: 0.8,

        stagger: 0.25,

        delay: 1.1

    });


    // Infinite floating movement

    gsap.to(".card-one", {

        y: -12,

        duration: 2,

        repeat: -1,

        yoyo: true,

        ease: "sine.inOut"

    });


    gsap.to(".card-two", {

        y: -10,

        duration: 2.4,

        repeat: -1,

        yoyo: true,

        ease: "sine.inOut"

    });


    gsap.to(".card-three", {

        y: -13,

        duration: 2.2,

        repeat: -1,

        yoyo: true,

        ease: "sine.inOut"

    });


    /* ==========================================
       HELP CARDS SCROLL ANIMATION
    ========================================== */

    gsap.from(".help-card", {

        scrollTrigger: {

            trigger: ".help-wrapper",

            start: "top 80%",

            toggleActions: "play none none reverse"

        },

        y: 70,

        opacity: 0,

        duration: 0.7,

        stagger: 0.12,

        ease: "power2.out"

    });


    /* ==========================================
       SECTION HEADINGS
    ========================================== */

    gsap.utils.toArray(".section-heading").forEach((heading) => {

        gsap.from(heading, {

            scrollTrigger: {

                trigger: heading,

                start: "top 85%",

                toggleActions: "play none none reverse"

            },

            y: 60,

            opacity: 0,

            duration: 0.8,

            ease: "power3.out"

        });

    });


    /* ==========================================
       SERVICE CARDS
    ========================================== */

    gsap.utils.toArray(".service-card").forEach((card, index) => {

        gsap.from(card, {

            scrollTrigger: {

                trigger: card,

                start: "top 88%",

                toggleActions: "play none none reverse"

            },

            y: 80,

            opacity: 0,

            scale: 0.94,

            duration: 0.7,

            delay: index * 0.05,

            ease: "power3.out"

        });

    });


    /* ==========================================
       SERVICE CARD HOVER
    ========================================== */

    document
        .querySelectorAll(".service-card")
        .forEach(card => {

            const image = card.querySelector("img");
            const arrow = card.querySelector(".service-body a");

            card.addEventListener("mouseenter", () => {

                gsap.to(image, {
                    scale: 1.07,
                    duration: 0.5,
                    ease: "power2.out"
                });

                gsap.to(arrow, {
                    x: 6,
                    duration: 0.3
                });

            });


            card.addEventListener("mouseleave", () => {

                gsap.to(image, {
                    scale: 1,
                    duration: 0.5
                });

                gsap.to(arrow, {
                    x: 0,
                    duration: 0.3
                });

            });

        });


    /* ==========================================
       STATS SECTION
    ========================================== */

    gsap.from(".stats-box", {

        scrollTrigger: {

            trigger: ".stats-box",

            start: "top 85%",

            toggleActions: "play none none reverse"

        },

        scale: 0.85,

        opacity: 0,

        duration: 1,

        ease: "power3.out"

    });


    /* ==========================================
       COUNTER ANIMATION
    ========================================== */

    document
        .querySelectorAll(".counter")
        .forEach(counter => {

            const target = parseInt(
                counter.innerText
            );

            counter.innerText = "0";

            gsap.to(counter, {

                scrollTrigger: {

                    trigger: counter,

                    start: "top 85%",

                    once: true

                },

                innerText: target,

                duration: 2,

                snap: {
                    innerText: 1
                },

                ease: "power2.out"

            });

        });


    /* ==========================================
       ABOUT IMAGE PARALLAX
    ========================================== */

    gsap.to(".about-image", {

        scrollTrigger: {

            trigger: ".about-section",

            start: "top bottom",

            end: "bottom top",

            scrub: true

        },

        y: -45,

        ease: "none"

    });


    /* ==========================================
       MISSION CARD
    ========================================== */

    gsap.from(".mission-card", {

        scrollTrigger: {

            trigger: ".about-section",

            start: "top 75%",

            toggleActions: "play none none reverse"

        },

        x: 80,

        opacity: 0,

        duration: 0.8,

        ease: "back.out(1.5)"

    });


    /* ==========================================
       ABOUT CONTENT
    ========================================== */

    gsap.from(".about-content > *", {

        scrollTrigger: {

            trigger: ".about-content",

            start: "top 78%",

            toggleActions: "play none none reverse"

        },

        x: 60,

        opacity: 0,

        duration: 0.7,

        stagger: 0.12,

        ease: "power3.out"

    });


    /* ==========================================
       EMERGENCY BOX
    ========================================== */

    gsap.from(".emergency-box", {

        scrollTrigger: {

            trigger: ".emergency-box",

            start: "top 80%",

            toggleActions: "play none none reverse"

        },

        x: 70,

        opacity: 0,

        duration: 0.8,

        ease: "power3.out"

    });


    /* ==========================================
       NEWS CARDS
    ========================================== */

    gsap.utils.toArray(".news-card").forEach((card, index) => {

        gsap.from(card, {

            scrollTrigger: {

                trigger: card,

                start: "top 88%",

                toggleActions: "play none none reverse"

            },

            y: 70,

            opacity: 0,

            duration: 0.8,

            delay: index * 0.12,

            ease: "power3.out"

        });

    });


    /* ==========================================
       CTA
    ========================================== */

    gsap.from(".cta-box", {

        scrollTrigger: {

            trigger: ".cta-box",

            start: "top 85%",

            toggleActions: "play none none reverse"

        },

        y: 70,

        opacity: 0,

        scale: 0.96,

        duration: 0.8,

        ease: "power3.out"

    });


    /* ==========================================
       FOOTER
    ========================================== */

    gsap.from(".footer .col-lg-3, .footer .col-lg-2", {

        scrollTrigger: {

            trigger: ".footer",

            start: "top 85%",

            toggleActions: "play none none reverse"

        },

        y: 40,

        opacity: 0,

        duration: 0.6,

        stagger: 0.1

    });


    /* ==========================================
       SMOOTH BUTTON HOVER
    ========================================== */

    document
        .querySelectorAll(
            ".primary-btn, .secondary-btn, .appointment-btn, .cta-btn"
        )
        .forEach(button => {

            button.addEventListener("mouseenter", () => {

                gsap.to(button, {

                    y: -3,

                    scale: 1.03,

                    duration: 0.25,

                    ease: "power2.out"

                });

            });


            button.addEventListener("mouseleave", () => {

                gsap.to(button, {

                    y: 0,

                    scale: 1,

                    duration: 0.25

                });

            });

        });


    /* ==========================================
       NAVBAR SCROLL EFFECT
    ========================================== */

    ScrollTrigger.create({

        start: "top -50",

        end: 99999,

        onUpdate: self => {

            if (self.direction === 1) {

                gsap.to(".main-navbar", {

                    boxShadow:
                        "0 5px 25px rgba(0,0,0,.08)",

                    duration: 0.3

                });

            } else {

                gsap.to(".main-navbar", {

                    boxShadow: "none",

                    duration: 0.3

                });

            }

        }

    });


    /* ==========================================
       REFRESH SCROLLTRIGGER
    ========================================== */

    window.addEventListener("load", () => {

        ScrollTrigger.refresh();

    });

});