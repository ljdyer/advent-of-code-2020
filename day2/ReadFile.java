
/**
 1. Read input.txt ☑
 2. Split by line ☑
 3. Split each line by colon
    (get rule, password) ☑
 4. Split rule to get (range, letter) ☑
 5. Iterate over passwords to find out 
    how many satisfy rule ☑
 */


import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.*;


public class ReadFile {
    public static void main(String[] args) {
        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            List<String> lines = new ArrayList<String>();
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                lines.add(data);
            }
            long numTrue = 0;
            for( String thisLine : lines ) {
                String[] parts = thisLine.split(":");
                String rule = parts[0];
                String password = parts[1];
                String[] ruleParts = rule.split(" ");
                String range = ruleParts[0];
                String letter = ruleParts[1];
                String[] rangeParts = range.split("-");
                String minStr = rangeParts[0];
                String maxStr = rangeParts[1];
                int min = Integer.parseInt(minStr);
                int max = Integer.parseInt(maxStr);
                
                int count = 0;
                for (int i = 0; i < password.length(); i++) {
                    if (password.charAt(i) == letter.charAt(0)) {
                        count++;
                    }
                }
                if (min <= count && max >= count){
                    numTrue = numTrue + 1;
                }
            }
            System.out.println(numTrue);
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
