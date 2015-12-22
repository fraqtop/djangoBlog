var bodo;
$(document).ready(function(){
    $('.like').click(function(){
        window.bodo = $(this).parent().get(0);
        $.ajax({
            url:"/liked/"+window.bodo.id,
            type:"GET",
            success:function(data){
                par = $(window.bodo).find($("p"));
                $(par).text(data['likes']);
            }
        });
    });
});
