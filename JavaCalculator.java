import java.util.Scanner;

public class JavaCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Читаем входные данные
        double number1 = scanner.nextDouble();
        double number2 = scanner.nextDouble();
        String operation = scanner.next();

        try {
            double result = calculate(number1, number2, operation);
            System.out.println(result);
        } catch (Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }

    public static double calculate(double number1, double number2, String operation) throws Exception {
        switch (operation) {
            case "+":
                return number1 + number2;
            case "-":
                return number1 - number2;
            case "*":
                return number1 * number2;
            case "/":
                if (number2 == 0) {
                    throw new ArithmeticException("ошибка, на ноль не делим");
                }
                return number1 / number2;
            case "**":
                return Math.pow(number1, number2);
            default:
                throw new IllegalArgumentException("неправильная операция");
        }
    }
}
