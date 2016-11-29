/**
 * Type.java
 * 17-Mar-2014 : 11:16:21 pm
 * 
 */
package head.first.OOAD.chapter05.RickGuitarV01;

/**
 * @author ubuntu
 * @packageName = head.first.OOAD.chapter05.RickGuitarV01:Type.java
 * @createdOn: 17-Mar-2014 : 11:16:21 pm
 * 
 * This is a file for my practice and notes of "Head First
 * OOAD, 1nd edition.".
 * Anyone can fork this repo, also the official code is available 
 * @(http://www.headfirstlabs.com/books/hfooad/)
 */
public enum Type {
	ACOUSTIC, ELECTRIC;

	  public String toString() {
	    switch(this) {
	      case ACOUSTIC: return "acoustic";
	      case ELECTRIC: return "electric";
	      default:       return "unspecified";
	    }
	  }
}
