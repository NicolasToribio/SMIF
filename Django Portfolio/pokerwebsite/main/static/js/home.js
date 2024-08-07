document.addEventListener("DOMContentLoaded", function () {
    const nameSearch = document.getElementById("name-search")
    const tags = document.querySelectorAll(".tag")
    const projects = document.querySelectorAll(".project")

    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase();

        projects.forEach((project) => { //searching through all of the different projects
            const name = project.getAttribute('data-name') //looking at the names of the projects
            const nameMatch = name.includes(nameQuery)

            if(nameMatch) {
                project.style.display = "" //keep the project if the name matches by keeping the display property blank
            } else {
                project.style.display = "none"; //otherwise we set the display to none, and effectively hide this element             
            }
        })
    }

    tags.forEach((tag) => { //similar function to above, but for the tags
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute("data-tag")

            project.forEach((project) => {
                const projectTags = project.getAttribute("data-tags")
                if (projectTags.includes(selectedTag)) {
                    project.style.display = ""
                } else {
                    project.style.display = "none"
                }
            })
        })
    })

    nameSearch.addEventListener("keyup", filterProjects)
})