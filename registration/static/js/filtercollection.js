const searchInput = document.getElementById('searchInput')
const collection = document.getElementById('filterList')
const collectionItemArray = Array.prototype.slice.call(collection.getElementsByTagName('a'))

const filterCollection = event => {
    const searchTerm = event.target.value.toLowerCase()
    collectionItemArray.forEach( a => {
        a.classList.add('hide')
        if (a.innerText.toLowerCase().indexOf(searchTerm) > -1) {
            a.classList.remove('hide')
        }
    })
}

searchInput.addEventListener('keyup', filterCollection, false)
