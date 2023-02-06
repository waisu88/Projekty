
    const gameArea = document.querySelector(".gameArea");
    const hole = document.querySelector(".hole");
    let player = document.querySelector(".player");
    let pavement = gameArea.getBoundingClientRect()
    let holeArea = hole.getBoundingClientRect()
    let enemy = {speed: 2}
    let ryan = document.querySelector(".player-image")
    let enemies = new Array()
    player.x = 10;
    player.y = 10;
    player.speed = 5;


    let keys = {
        Space: false,
        Escape: false
    }



    function onMouseClick(event) {
        destinationX = event.x - (30 + pavement.left);
        destinationY = event.y - (30 + pavement.top);
        console.log(destinationX, destinationY)
        let differenceBeetwenX = destinationX - player.x
        let differenceBeetwenY = destinationY - player.y 
        xSpeedShare = differenceBeetwenX/(Math.abs(differenceBeetwenX) + Math.abs(differenceBeetwenY))*7
        ySpeedShare = differenceBeetwenY/(Math.abs(differenceBeetwenX) + Math.abs(differenceBeetwenY))*7

        
        let rotateValue = Math.atan2(differenceBeetwenY, differenceBeetwenX)*180/Math.PI
        ryan.style.transform = "rotate(" + Math.trunc(rotateValue) + "deg)"
        


        let aspiranto = document.querySelectorAll(".aspirant")
        aspiranto.forEach(function(item) {
            item.setspeed = true;
        }
        )
    }   



    function ridePlayer() {
        if (player.x > 0 && player.x < pavement.bottom && player.y > 0 && player.y < pavement.right){
            if (Math.abs(destinationX - player.x) > 3){
                player.x += xSpeedShare
            }
            if (Math.abs(destinationY - player.y) > 3){
                player.y += ySpeedShare
            }

            player.style.left = player.x + 'px';
            player.style.top = player.y + 'px';
        }
    }

        
    // pavement.addEventListener('mouseout', stopGame)
    // pavement.addEventListener('mouseenter', startGame)
    

    function startGame () {
        window.requestAnimationFrame(playGame)
    }
   
    document.addEventListener('keydown', pressKey)
    gameArea.addEventListener('click', onMouseClick);
    

    function pressKey(event) {
        event.preventDefault();
        console.log(keys)
        if (event.key == " "){
            keys.Space = true;
            keys.Escape = false
        }
        keys[event.key] = true;
        if (keys.Escape) {
            keys.Space = false
            window.requestAnimationFrame(playGame)
        }
    }

    gameArea.appendChild(player)




    function createAspirants() {
        for(let x=0; x<5; x++){
            let aspirant = document.createElement("div")
            aspirant.classList.add("aspirant")
           
            aspirant.x = (-1) * 100
            aspirant.y = Math.floor(Math.random()*500)
            aspirant.xSpeed = 3
            aspirant.ySpeed = 0        
            aspirant.style.left = aspirant.x + "px";
            aspirant.style.top = aspirant.y + "px" 
            enemies.push(aspirant)
            gameArea.appendChild(aspirant)
        }
    }


    function moveAspirants() {
        
        enemies.forEach(function(item) {

            
            item.y += 1
            item.x += 1

            item.style.left = item.x + "px";
            item.style.top = item.y + "px";

           
            if (item.x > pavement.bottom || item.y > pavement.right ) {
                let diffPlayerAspX = player.x - item.x
                let diffPlayerAspY = player.y - item.y
                xSpeedAsp = diffPlayerAspX/(Math.abs(diffPlayerAspX) + Math.abs(diffPlayerAspY))*5
                ySpeedAsp = diffPlayerAspY/(Math.abs(diffPlayerAspX) + Math.abs(diffPlayerAspY))*5
                item.xSpeed = xSpeedAsp
                item.ySpeed = ySpeedAsp
                item.x = 50
                item.y = Math.floor(Math.random()*500)
            }

        })
    }
    let destinationX = 500;
    let destinationY = 500;
    let xSpeedShare = 0
    let ySpeedShare = 0
    let rotateValue = 0
    let xSpeedAsp = 3
    let ySpeedAsp = 3
    let updateSpeed = false


    function playGame() {
        // movePlayer();

        ridePlayer();
        
        
        moveAspirants();
        if (!keys.Space) {
          window.requestAnimationFrame(playGame)  
        }
        
    }
    window.requestAnimationFrame(playGame)
    createAspirants()

 