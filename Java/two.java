package com.akshat;

public class two {
    private int height;
    private int weight;
    private String name;

    public two(int height, int weight, String name){
        this.height=height;
        this.weight=weight;
        this.name=name;
    }


    public void printData(){
        System.out.println(height);
        System.out.println(weight);
        System.out.println(name);
    }
}

class Professional extends two{
    private String profession;

    public Professional(int height, int weight, String name, String profession){
        super(height, weight, name);
        this.profession=profession;
    }


    public void dataOut(){
        printData();
        System.out.println(profession);
    }

    public static void main(String[] args) {
        Professional Rahul=new Professional(180,75,"Rahul Badalandabad","Savage");
        Rahul.dataOut();

    }
}


