import java.util.Scanner;
public class Account {
public static void main(String[] args) {

Scanner input = new Scanner(System.in);
int pick = 0;
int account = 0;
while(pick != -1){

	System.out.print("press 1 to deposit, press 2 to withdraw and -1 to see your balance: ");
	pick = input.nextInt();
	if(pick == 1){
		System.out.print("deposit: ");
		int deposit = input.nextInt();
		account += deposit; 
	}else if(pick == 2){
		System.out.print("withdraw: ");
		int withdraw  = input.nextInt();
		account -= withdraw;
	}
 }
	System.out.print(account);



}}