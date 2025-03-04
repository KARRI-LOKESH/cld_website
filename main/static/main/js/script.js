console.log("College website loaded successfully!");
document.addEventListener("DOMContentLoaded", function () {
    gsap.from("nav a", { opacity: 0, y: -50, duration: 1, stagger: 0.2 });
    gsap.from("h1", { opacity: 0, x: -100, duration: 1, delay: 0.5 });
    gsap.from("img", { opacity: 0, scale: 0.5, duration: 1, delay: 1 });

    document.querySelectorAll("button").forEach((btn) => {
        btn.addEventListener("click", function () {
            gsap.to(btn, { scale: 0.9, duration: 0.1, yoyo: true, repeat: 1 });
        });
    });
});

