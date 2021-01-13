function calculate() {
    var Num = document.getElementById("Number").value;
    text = "";
    if (isNaN(Num)){
        document.getElementById("Output").value= "Please enter a valid number"
    }else{
        for (i=0; i<10; i++){
            count = 0;
            for (j=0;j<Num.length;j++) {
                if (Num.charAt(j)==i){count += 1;}
                
            }
            
            if (count != 0){
                if (count == 1){
                    text += "Number " + i + " appears " + count + " time.\r\n"
                } else{
                    text += "Number " + i + " appears " + count + " times.\r\n"
                }
            }
        }
        document.getElementById("Output").value= text
    }
}
