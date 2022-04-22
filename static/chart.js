window.onload=()=>{
    build_ul_chart()
    build_ur_chart()
    build_ll_chart()
    build_lr_chart()
}

// UPPER LEFT CHART

async function build_ul_chart(){
    const data = await fetchAPI('views-time',{'year':2021,'month':false,'unique':false,'type':'views'})

    const label = 'Views over 2021'
    const x = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    // const y = [0,10,5,2,20,30,45]

    // const x = data.x
    const y = data.y

    draw_ul_chart(x,y,label)
}


function draw_ul_chart(xdata,ydata,label){
    const ul_xLabs = xdata
    const ul_ycoord = ydata

    const ul_data = {
        labels:ul_xLabs,
        datasets:[
            {
                label:label,
                borderColor:'rgb(255,99,132)',
                data:ul_ycoord
            }
        ]
    };

    const ul_config = {
        type:'line',
        data:ul_data,
        options: {
            plugins:{
                title:{
                    display:true,
                    text:'Page views per month',
                    fullSize:true,
                    font:{
                        size:24,
                    }
                },
                legend:{
                    display:false,
                }
            }
        }
    }

    const ulChart = new Chart(
        document.getElementById('ul-chart'),
        ul_config
    )
}


// UPPER RIGHT KPI



async function build_ur_chart(year=2020,month=12){
    data_av = await fetchAPI('kpi',{'request':'KPI_av','year':year,'month':month})
    data_goal = await fetchAPI('kpi',{'request':'KPI_goal','year':year,'month':month})
    
    
    kpi1 = document.getElementById('kpi1');
    kpi2 = document.getElementById('kpi2');
    draw_circle(kpi1,data_av.fillColor,data_av.kpi,'av views');
    draw_circle(kpi2,data_goal.fillColor,data_goal.kpi+'%','mo. goal');
}

function draw_circle(canvas,color,kpi,message){
    c = canvas.getContext('2d');
    c.beginPath();
    c.fillStyle='white';
    c.height = 250;
    c.width = 250;
    x = c.width / 2;
    y = c.height / 2;
    c.arc(x,y, 100, 0, 2*Math.PI, false);
    c.fill();

    c.lineWidth = 8;
    c.strokeStyle = color;
    c.stroke();

    c.beginPath();
    c.fillStyle='black';
    c.font = '40px Ariel';

    if (message=='av views'){
        c.fillText(kpi,x-23,y)
        c.font = '20px Ariel';
        c.fillText(message,x-32,y+40)
    }else{
        c.fillText(kpi,x-40,y)
        c.font = '20px Ariel';
        c.fillText(message,x-32,y+40)
    }
    c.fill()


}


// LOWER LEFT CHART

async function build_ll_chart(){
    const data = await fetchAPI('views-type',{'type':'subs'})

    const label = 'subs by topic'
    // const x = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    // const y = [0,10,5,2,20,30,45]

    const x = data.x
    const y = data.y

    draw_ll_chart(x,y,label)
}


function draw_ll_chart(xdata,ydata,label){
    const ul_xLabs = xdata
    const ul_ycoord = ydata

    const ul_data = {
        labels:ul_xLabs,
        datasets:[
            {
                label:label,
                borderColor:'rgb(255,99,132)',
                data:ul_ycoord,
                backgroundColor:[
                    'rgba(54, 162, 235, 0.4)'
                ]
            }
        ]
    };

    const ul_config = {
        type:'bar',
        data:ul_data,
        options: {
            plugins:{
                title:{
                    display:true,
                    text:'Subscribers per Topic',
                    fullSize:true,
                    font:{
                        size:24,
                    }
                },
                legend:{
                    display:false,
                }
            },
            indexAxis:'y',
        }
    }

    const ulChart = new Chart(
        document.getElementById('ll-chart'),
        ul_config
    )
}



// LOWER RIGHT CHART


async function build_lr_chart(){
    //Call for author list
    const data = await fetchAPI('authors',{'year':2021,'month':false,'unique':false})

    for (i=0;i<data.length;i++){
        let row = data[i]
        let user_wrapper = document.createElement('div')
        user_wrapper.classList.add('stats-author')
        user_wrapper.id = "stats-"+row[i].author.replace(/\s/g,"_");
        

    }



    const label = 'Views over 2021'
    const x = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    // const y = [0,10,5,2,20,30,45]

    // const x = data.x
    const y = data.y

    draw_ul_chart(x,y,label)
}


function draw_lr_chart(xdata,ydata,domID){
    const ul_xLabs = xdata
    const ul_ycoord = ydata

    const ul_data = {
        labels:ul_xLabs,
        datasets:[
            {
                label:label,
                borderColor:'rgb(255,99,132)',
                data:ul_ycoord
            }
        ]
    };

    const ul_config = {
        type:'line',
        data:ul_data,
        options: {
            plugins:{
                title:{
                    display:true,
                    text:'Page views per month',
                    fullSize:true,
                    font:{
                        size:24,
                    }
                },
                legend:{
                    display:false,
                }
            }
        }
    }

    const ulChart = new Chart(
        domID,
        ul_config
    )
}

function make_avatar(link){
    img = document.createElement('img');
    img.src = link;
    img.alt = "avatar from Pixabay.com";
    return img
}

function make_name(name,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = name;
    return p
}

function make_post_stat(stat,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = stat;
    return p
}

function make_revenue_stat(stat,i){
    p = document.createElement('p');
    p.classList.add('stat-author-item','stat-author-item-'+i);
    p.innerText = stat;
    return p
}

function make_sparkline(data){
    div = document.createElement('p');
    div.classList.add('stats-sparkline','stat-author-item','stat-author-item-'+i);
    
    let xdata = data[]
    draw_lr_chart(xdata,ydata,div)


    return div
}