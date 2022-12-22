

/** Alerta personalizadas */
function mensajeAlerta(msg, tipo_msg='') {
    let text  = document.querySelector('.text-2').textContent = `${msg}`;

    const toast    = document.querySelector(".toast");
        closeIcon  = document.querySelector(".close"),
        progress   = document.querySelector(".progress");


    toast.classList.add("active");
    progress.classList.add("active");

    setTimeout(() => {
        toast.classList.remove("active");
    }, 5000);

    closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
    });
}


/**Ocultando la alerta que se dispara sin el JavaScript */
let verificar_clase = $(".mi_alerta").hasClass("active")
console.log(verificar_clase);
if(verificar_clase ==true){
    setTimeout(() => {
        $(".mi_alerta").removeClass("active");
    }, 5000);
}