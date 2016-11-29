/**
 * DogDoorSimulator.java
 * 06-Mar-2014 : 11:07:47 pm
 * 
 */
package head.first.OOAD.chapter04.DogDoorV04;

/**
 * @author ubuntu
 * @packageName = head.first.OOAD.chapter04.DogDoorV04:DogDoorSimulator.java
 * @createdOn: 06-Mar-2014 : 11:07:47 pm
 * 
 * This is a file for my practice and notes of "Head First
 * OOAD, 1nd edition.".
 * Anyone can fork this repo, also the official code is available 
 * @(http://www.headfirstlabs.com/books/hfooad/)
 */
public class DogDoorSimulator {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DogDoor door = new DogDoor();
	    door.addAllowedBark(new Bark("rowlf"));
	    door.addAllowedBark(new Bark("rooowlf"));
	    door.addAllowedBark(new Bark("rawlf"));
	    door.addAllowedBark(new Bark("woof"));
	    BarkRecognizer recognizer = new BarkRecognizer(door);
	    Remote remote = new Remote(door);
	    
	 // Simulate the hardware hearing a bark
	    System.out.println("Bruce starts barking.");
	    recognizer.recognize(new Bark("Rowlf"));

	    System.out.println("\nBruce has gone outside...");

	    try {
	      Thread.currentThread().sleep(10000);
	    } catch (InterruptedException e) { }

	    System.out.println("\nBruce all done...");
	    System.out.println("...but he's stuck outside!");

	    // Simulate the hardware hearing a bark (not Bruce!)
	    Bark smallDogBark = new Bark("yip");
	    System.out.println("A small dog starts barking.");
	    recognizer.recognize(smallDogBark);

	    try {
	      Thread.currentThread().sleep(5000);
	    } catch (InterruptedException e) { }

	    // Simulate the hardware hearing a bark again
	    System.out.println("\nBruce starts barking.");
	    recognizer.recognize(new Bark("Rowlf"));

	    System.out.println("\nBruce's back inside...");

	}

}
