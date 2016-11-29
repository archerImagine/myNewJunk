package com.cisco.cmad.repository;

import com.cisco.cmad.model.BlogUser;

public class BlogUserRepositoryStub implements BlogUserRepository {

	@Override
	public void create(BlogUser blogUser) {
		// TODO Connect to Database here.
		
		System.out.println("BlogUserRepositoryStub.create()");
		
	}

}
