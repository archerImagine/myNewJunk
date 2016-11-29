/**
 * Builder.java
 * 18-Mar-2014 : 10:10:25 pm
 * 
 */
package head.first.OOAD.chapter05.RickGuitarV02;

/**
 * @author ubuntu
 * @packageName = head.first.OOAD.chapter05.RickGuitarV02:Builder.java
 * @createdOn: 18-Mar-2014 : 10:10:25 pm
 * 
 * This is a file for my practice and notes of "Head First
 * OOAD, 1nd edition.".
 * Anyone can fork this repo, also the official code is available 
 * @(http://www.headfirstlabs.com/books/hfooad/)
 */
public enum Builder {
	FENDER, MARTIN, GIBSON, COLLINGS, OLSON, RYAN, PRS, ANY;

	  public String toString() {
	    switch(this) {
	      case FENDER:   return "Fender";
	      case MARTIN:   return "Martin";
	      case GIBSON:   return "Gibson";
	      case COLLINGS: return "Collings";
	      case OLSON:    return "Olson";
	      case RYAN:     return "Ryan";
	      case PRS :     return "PRS";
	      default:       return "Unspecified";
	    }
	  }
}
