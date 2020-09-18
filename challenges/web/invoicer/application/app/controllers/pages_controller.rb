class PagesController < ApplicationController  
  before_action do
    if current_user.demo
      flash[:danger] = 'Forbidden: your account is limited to the basic feature.'
      redirect_to :root
    end
  end

  def metrics
    @flag = ENV['FLAG_2']
    render :metrics
  end
end
