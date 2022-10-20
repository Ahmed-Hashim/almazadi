;(function(){

const toastElement = document.getElementById("toast")
const toastBody = document.getElementById("toast-body")

const toast = new bootstrap.Toast(toastElement, { delay: 2000 })
htmx.on("type", (e) => {
  toastElement.classList.remove("bg-primary");
  toastElement.classList.remove("bg-secondary");
  toastElement.classList.remove("bg-success");
  toastElement.classList.remove("bg-danger");
  toastElement.classList.remove("bg-warning");
  toastElement.classList.remove("bg-info");
  toastElement.classList.remove("bg-light");
  toastElement.classList.remove("bg-dark");
  toastElement.classList.add(e.detail.value);
})
htmx.on("showMessage", (e) => {
  toastBody.innerText = e.detail.value
  toast.show()
})


})()

;(function(){
  const modal = new bootstrap.Modal(document.getElementById("modal"))

  htmx.on("htmx:afterSwap", (e) => {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id == "dialog") {
      modal.show()
    }
  })
  htmx.on("close", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.value=="close") {
        modal.hide()
      e.detail.shouldSwap = false
    }


      
    
  })
  })()