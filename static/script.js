
function search(){
    console.log('you found me');
    const form = document.getElementById('searchbar');
    searchobj = {"search":form.childNodes[1].value}

    fetch('/search/',{
        method: 'POST',
        credentials:'same-origin',
        mode:'cors',
        headers: {
            'Content-Type':'application/json',
        },
        body: JSON.stringify(searchobj),
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        if(!data.response){
            noResults()
        }
        else{
            populate(data['answer'])
        }
    })
}

function populate(results){
    container = document.getElementById('results');
    container.innerHTML = "";
    console.log('got to pupulate')
    console.log(results.length)
    for (i=0;i<results.length;i++){
        console.log(i)
        let wrapper, h3, p, a 
        [wrapper,h3,p,a]= makeFeed();
        h3.innerText = results[i][0];
        p.innerText = results[i][2];
        a.href = "/topic/"+results[i][1]+"/"+results[i][0];
        a.appendChild(h3);
        a.appendChild(p);
        wrapper.appendChild(a);
        container.appendChild(wrapper);
    }
}


function noResults(){
    container = document.getElementById('results');
    container.innerHTML = '';
    h3 = document.createElement('h3');
    h3.innerText = 'There are no search results';
    container.appendChild(h3);
}

function makeFeed(){
    wrapper = document.createElement('div');
    wrapper.classList.add('search-results');
    a = document.createElement('a');
    a.classList.add('result-a');
    h3 = document.createElement('h3');
    h3.classList.add('title');
    p = document.createElement('p');
    p.classList.add('preview');

    return [wrapper,h3,p,a]
}