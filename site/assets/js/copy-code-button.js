function addCopyButtons(clipboard) {
    document.addEventListener("DOMContentLoaded", function() {
        document.querySelectorAll("pre code").forEach(codeBlock => {
            var button = document.createElement("button");
            button.innerText = "Copy";
            button.classList.add("copy-code");
    
            let preBlock = codeBlock.closest("pre");
            preBlock.style.position = "relative"; // Ensure parent is positioned
            preBlock.appendChild(button);
    
        button.addEventListener('click', function() {
            clipboard.writeText(codeBlock.textContent).then(
                function() {
                    /* Chrome doesn't seem to blur automatically, leaving the button
                       in a focused state */
                    button.blur();

                    button.innerText = 'Copied!';
                    setTimeout(function() {
                        button.innerText = 'Copy';
                    }, 2000);
                },
                function(error) {
                    button.innerText = 'Error';
                    console.error(error);
                }
            );
        });
    
            // Ensure button appears only on hover
            preBlock.addEventListener("mouseenter", () => {
                button.style.display = "block";
            });
            preBlock.addEventListener("mouseleave", () => {
                button.style.display = "none";
            });
        });
    });
}

if (navigator && navigator.clipboard) {
    addCopyButtons(navigator.clipboard);
} else {
    var script = document.createElement('script');
    script.src =
        'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
    script.integrity = 'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
    script.crossOrigin = 'anonymous';

    script.onload = function() {
        addCopyButtons(clipboard);
    };

    document.body.appendChild(script);
}