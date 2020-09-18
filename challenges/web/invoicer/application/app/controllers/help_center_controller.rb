class HelpCenterController < ApplicationController
  skip_before_action :authenticate!
  layout 'help_center'

  def home
    render :home
  end

  def password_reset
    render :password_reset
  end

  def search_invoice
    render :search_invoice
  end
end
