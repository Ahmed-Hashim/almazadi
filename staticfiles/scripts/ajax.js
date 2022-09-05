const deleteAjax = document.querySelectorAll('#deleteAjax');
const deleteArray= [...deleteAjax];
const rowsAjax = document.querySelectorAll('#rows');
const rowsArray= [...rowsAjax];
const spinner=document.getElementById("spinner-box");

deleteAjax.forEach(btn=>{
    btn.addEventListener('click',e=>{
        console.log('delete_post_ajax/p='+btn.getAttribute("name"))
        $.ajax({
            url:'delete_post_ajax/p='+btn.getAttribute("name"),
            success:function(response){
                spinner.classList.remove('visible');
                rowsArray.forEach(item=>{
                    if (item.getAttribute("name")==btn.getAttribute("name")){
                        item.classList.add('loader');
                        item.classList.add('fadeout');
                        
                        setTimeout( () =>{
                            item.remove();
                            spinner.classList.add('visible');
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
