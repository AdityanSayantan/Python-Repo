import java.util.Scanner;

public class HexToBinaryConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input: number of queries
        int Q = scanner.nextInt();
        scanner.nextLine();  // Consume the newline

        for (int i = 0; i < Q; i++) {
            // Read each hexadecimal number
            String hex = scanner.nextLine();

            // Convert hexadecimal to decimal
            int decimal = Integer.parseInt(hex, 16);

            // Convert decimal to binary
            String binary = Integer.toBinaryString(decimal);

            // Format binary to include leading zeros
            int desiredLength = hex.length() * 4;  // Each hex digit corresponds to 4 binary digits
            String formattedBinary = String.format("%" + desiredLength + "s", binary).replace(' ', '0');

            // Output the binary representation
            System.out.println(formattedBinary);
        }

        scanner.close();
    }
}