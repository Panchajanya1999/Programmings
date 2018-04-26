import java.util.Scanner;
class Armstrong {

    public static void main(String[] args) {

        int num , number, temp, total = 0;
        System.out.println("Enter the number :");
        num=new Scanner(System.in).nextInt();
        number = num;
        while (number != 0)
        {
            temp = number % 10;
            total = total + temp*temp*temp;
            number /= 10;
        }

        if(total == num)
            System.out.println(num + " is an Armstrong number");
        else
            System.out.println(num + " is not an Armstrong number");
    }
}
