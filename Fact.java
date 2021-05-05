import java.util.*;
class Factorial{  
 public static void main(String args[]){  
  int i,fact=1;  
  int number;//It is the number to calculate factorial  
Scanner s=new Scanner(System.in);
System.out.println("enter a number");
number=s.nextInt();  
  for(i=1;i<=number;i++){    
      fact=fact*i;    
  }    
  System.out.println("Factorial of "+number+" is: "+fact);    
 }  
}  