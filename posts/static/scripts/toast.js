;(function(){

const toastElement = document.getElementById("toast")
const toastBody = document.getElementById("toast-body")

const toast = new bootstrap.Toast(toastElement, { delay: 2000 })
htmx.on("type", (e) => {
  toastElement.classList.add(e.detail.value);
})
htmx.on("showMessage", (e) => {
  console.log(e.detail.value)
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
  htmx.on("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {

      modal.hide()
      e.detail.shouldSwap = false
    }


      
    
  })
  })()