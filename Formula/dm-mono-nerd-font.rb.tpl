class DmMonoNerdFont
  desc "DM Mono with Nerd Fonts glyphs"
  homepage "https://github.com/kilork/dm-mono-nerd-font"
  version "{{VERSION}}"

  url "https://github.com/kilork/dm-mono-nerd-font/releases/download/v{{VERSION}}/dm-mono-nerd-font-{{VERSION}}.tar.gz"
  sha256 "{{SHA256}}"

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