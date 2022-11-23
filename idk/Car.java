public class Car {
    String color;
    boolean isElectric;
    int cupHolders;
   
    public static void main(String[] args) {
      Car myCar = new Car();
      myCar.color = "Red";
      myCar.isElectric = false;
      myCar.cupHolders = 4;
      System.out.println("Color: " + myCar.color); 
      System.out.println("isElectric: " + myCar.isElectric); 
      System.out.println("cupHolders: " + myCar.cupHolders); 
  }
}