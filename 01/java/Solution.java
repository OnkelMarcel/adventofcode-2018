public class Solution {

	static List<String> liste = new ArrayList<>();

	public static void main(String[] args) {
		read();
		int x = 0;

		for (String l : liste) {

			if (l.startsWith("+")) {
				
				String[] split = l.split("\\+");
				x += Integer.valueOf(split[1]);
				
			} else if (l.startsWith("-")) {
				
				String[] split = l.split("\\-");
				x -= Integer.valueOf(split[1]);
				
			}
			
		}
		
		System.out.println(x);
	}

	public static void read() {

		try {
			BufferedReader reader = new BufferedReader(new FileReader(new File(PathToYourInput)));
			String line = "";

			while ((line = reader.readLine()) != null) {
				liste.add(line);
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
  //#ShitCode
}
