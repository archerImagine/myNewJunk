package com.udacity.cs046.chapter02;

/**
 * Created by animeshb on 16/8/16.
 */
public class DayTest {


    public static void main(String[] args) {
        Day newDay = new Day(1964,11,28);
        System.out.println("[AniB]: Day: " +newDay.toString());

        newDay.addDays(228);
        System.out.println("[AniB]: Day: " +newDay.toString());

        Day birthday = new Day(1951, 5, 26);
        Day lastDay = new Day(2012, 7, 23);

        System.out.println(lastDay.daysFrom(birthday));
    }
}
