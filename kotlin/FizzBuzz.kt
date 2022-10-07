package testLogic

fun main() {
    /*print("Enter a number = ")
    var number = Integer.valueOf(readLine())*/

    for (num in 1..100){
        if(num % 2 == 1){
            if(num % 9 == 0){
                println("$num Mampu")
            }
            println("Mam")
        }else if(num % 5 == 0){
            println("pu")
        }else{
            println(num)
        }
    }
}