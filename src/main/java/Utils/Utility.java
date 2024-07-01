package Utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Utility {

	public static final int IMPLICIT_WAIT_TIME=30;
	public static final int PAGE_WAIT_TIME=5;
	
	
	
	 public static Object[][] getDataFromCsv(String filePath) throws IOException {
		    String COMMA_DELIMITER = ",";
		    List<List<String>> records = new ArrayList<>();
		    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
		        String line;
		        while ((line = br.readLine()) != null) {
		            String[] values = line.split(COMMA_DELIMITER);
		            records.add(Arrays.asList(values));
		        }
		    } catch (Exception e) {
		        e.printStackTrace();
		    }

		    // Debugging: Print the records read from the CSV
		    System.out.println("Records from CSV:");
		    for (List<String> record : records) {
		        System.out.println(record);
		    }

		    // Check if the records list is not empty and the first row has the expected number of columns
		    if (records.size() > 1 && records.get(0).size() == 14) {
		        Object[][] data = new Object[records.size() - 1][records.get(0).size()];
		        for (int r = 1; r < records.size(); r++) {
		            for (int c = 0; c < records.get(r).size(); c++) {
		                data[r - 1][c] = records.get(r).get(c);
		            }
		        }
		        return data;
		    } else {
		        throw new RuntimeException("CSV file does not have the expected number of rows or columns.");
		    }
	 }
}
	

