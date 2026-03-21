class DmMonoNerdFont
  desc "DM Mono with Nerd Fonts glyphs"
  homepage "https://github.com/kilork/dm-mono-nerd-font"
  version "3.4.0"

  url "https://github.com/kilork/dm-mono-nerd-font/releases/download/v#{version}/dm-mono-nerd-font-#{version}.tar.gz"
  sha256 "TODO"

  def install
    font_dir = Pathname.new(ENV["HOME"])/"Library/Fonts"
    font_dir.mkpath

    Dir["*.ttf"].each do |font|
      cp font, font_dir
    end
  end

  test do
  end
end