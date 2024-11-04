import java.util.Scanner;
public class demo{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
      //  int f = sc.nextInt();
        double f =((9*c + 160)/(double)5);
        System.out.printf("%.2f",f);
    }
}