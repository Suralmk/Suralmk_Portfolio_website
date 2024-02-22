const copyField = document.querySelectorAll(".copy-field")

copyField.forEach(  (copy) => {
    copy.querySelector("button").addEventListener("click", () => {
        copy.querySelector("input").select()
        document.execCommand("copy") 
        copy.classList.add("copied")
        window.getSelection().removeAllRanges()
        setTimeout(() => {
            copy.classList.remove("copied")
        }, 2000)
    })
}) 