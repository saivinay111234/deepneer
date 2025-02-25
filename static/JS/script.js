document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".category h3").forEach(category => {
        category.addEventListener("click", function() {
            let sublist = this.nextElementSibling;
            if (sublist) {
                sublist.classList.toggle("hidden");
            }
        });
    });

    // Prevent locked topics from navigating
    document.querySelectorAll(".locked").forEach(item => {
        item.addEventListener("click", function(event) {
            event.preventDefault();
            alert("🔒 This topic is locked! It will be unlocked soon.");
        });
    });
});
