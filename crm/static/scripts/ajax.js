const deleteAjax = document.querySelectorAll('#deleteAjax');
const deleteArray= [...deleteAjax];
const rowsAjax = document.querySelectorAll('#rows');
const rowsArray= [...rowsAjax];


deleteAjax.forEach(btn=>{
    btn.addEventListener('click',e=>{

        $.ajax({
            url:'delete_post_ajax/p='+btn.getAttribute("name"),
            success:function(response){
                rowsArray.forEach(item=>{
                    if (item.getAttribute("name")==btn.getAttribute("name")){
                        const targetbtn = document.getElementById(`target-${btn.getAttribute("name")}`)
                        console.log()
                        targetbtn.innerHTML='<span class="spinner-border spinner-border-sm" role="status"></span>';
                        item.classList.add('loader');
                        item.classList.add('fadeout');
                        setTimeout( () =>{
                            item.remove();
                        }, 2000);
                    };
                })
            },
            error:function(error){
                console.error();
            }
        })
    });

});
