(function(){

    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Seguro De Eliminar La Ficha?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();