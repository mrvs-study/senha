import java.util.Scanner;

public class fatoria {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número inteiro não negativo: ");
        int numero = scanner.nextInt();
        
        if (numero < 0) {
            System.out.println("Por favor, digite um número inteiro não negativo.");
        } else {
            long resultado = calcularFatorial(numero);
            System.out.println(numero + "! = " + resultado);
        }
        
        scanner.close();
    }
    
    public static long calcularFatorial(int numero) {
        if (numero == 0 || numero == 1) {
            return 1;
        } else {
            long fatorial = 1;
            for (int i = 2; i <= numero; i++) {
                fatorial *= i;
            }
            return fatorial;
        }
    }
}
