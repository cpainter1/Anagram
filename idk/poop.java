import java.lang.Math;

public class poop {

    public static double cube(double numberToCube) {
        double cubedNum = Math.pow(numberToCube, 3);
        return cubedNum;
    }
    public static void main(String[] args) {
        System.out.println(cube(3));
        
    }
}
