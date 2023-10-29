//Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido//

import java.util.Scanner;

public class senha {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite a senha");
        int senha = sc.nextInt();
        if(senha==1234) {
            System.out.println("a senha digitada está correta");
        }
        else{
System.out.println("deseja tentar novamente?(S/N)");
        char escolha = sc.next().charAt(0);
        if (escolha == 'S') {
            System.out.println("digite a senha novamente");
            senha = sc.nextInt();
            if (senha !=1234){
            System.out.println("você errou a senha novamente."+"\n"+"programa encerrado");
            }
            else{System.out.println("você acertou, bem-vindo");}
        }
        else{}
        
            
        } 
    }
}
