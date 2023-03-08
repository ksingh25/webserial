
function reloadData(url, html_id)
{
    var req = new XMLHttpRequest();
    var now = new Date();
    req.open("GET", url + "?" + now.getTime(), false);
    req.onreadystatechange = function ()
    {
        if(req.readyState === 4)
        {
            if(req.status === 200 || req.status == 0)
            {
                 dataDiv = document.getElementById(html_id);
                 dataDiv.innerHTML = req.responseText.split("\n").reverse().slice(0, 1000).join("\n");

            }
        }
    }
    req.send(null);
}


function reloadFiles() 
{
    reloadData("sensor.txt", "sensor1");
}

setInterval(reloadFiles, 1000);
