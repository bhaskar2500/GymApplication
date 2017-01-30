$(document).ready(function(){

$('a').each(function(){ 
    if($(this).text()=='View site') 
        $(this).attr('href','/Auth') });
});