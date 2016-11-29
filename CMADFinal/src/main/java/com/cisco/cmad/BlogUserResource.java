package com.cisco.cmad;

import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import com.cisco.cmad.model.BlogUser;
import com.cisco.cmad.repository.BlogUserRepository;
import com.cisco.cmad.repository.BlogUserRepositoryStub;

/**
 * Root resource (exposed at "myresource" path)
 */
@Path("/resource")
public class BlogUserResource {
	private BlogUserRepository blogUserRepository = new BlogUserRepositoryStub();
	@POST
	@Path("signup")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public Response createBlogUser(BlogUser blogUser){
		System.out.println("BlogUserResource.createBlogUser() : " +blogUser.getEmail());
		System.out.println("BlogUserResource.createBlogUser() : " +blogUser.getPassword());
		System.out.println("BlogUserResource.createBlogUser() : " +blogUser.getUserName());
		
		blogUserRepository.create(blogUser);
		
		return Response.ok().build();
	}
	
}
