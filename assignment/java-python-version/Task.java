import java.util.Scanner;
public class Task{

public static void main(String[] args) {
Scanner input = new Scanner(System.in);


System.out.println("enter car price");
int price = input.nextInt();


if(price <= 1000000){
	System.out.println("tax is : " + price * 0.1);
}
else if(price > 1000000 && price <= 3000000 ){
	System.out.println("tax is : "+ price * 0.15);
}
else if (price > 3000000 && price < 5000000 ){
System.out.println("tax is : " + price * 0.2);
}
else if (price >= 5000000 ){
	System.out.println("tax is : " + price * 0.25);
}



}

}