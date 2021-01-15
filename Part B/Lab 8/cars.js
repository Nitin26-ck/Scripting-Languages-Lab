window.onload=function()
{
    var teslaModels = [
        {
            "model":"modelS",
            "name":"Model S",
            "year": 2017,
            "price": 69200
        },
        {
            "model":"modelX",
            "name":"Model X",
            "year": 2015,
            "price": 55000
        },
        {
            "model":"model3",
            "name":"Model 3",
            "year": 2018,
            "price": 74500
        }
    ];


    teslaModels.forEach(function(item,index) 
    {
        listElement=document.createElement("th")
        listElement.id=item.model
        listElement.innerHTML=item.name
        document.getElementById("menu").appendChild(listElement)
    
    })

    teslaModels.forEach(mouseOverHandler);
    function mouseOverHandler(item,index)
    {
        var ele=document.getElementById(item.model);
        ele.onmouseover=function()
        {
            var details=item;
            if(details!=null)
            {
                document.getElementById("data-table").removeAttribute('hidden');
                document.getElementById("model").innerHTML=details.name;
                document.getElementById("picture").innerHTML='<img src="img'+details.model+'.png"/>';
                document.getElementById("year").innerHTML=details.year;
                document.getElementById("price").innerHTML="$"+details.price;
            }
        }
    }
};