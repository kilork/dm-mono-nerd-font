class DmMonoNerdFont < Formula
  desc "DM Mono with Nerd Fonts glyphs"
  homepage "https://github.com/kilork/dm-mono-nerd-font"
  version "3.4.0"

  url "https://github.com/kilork/dm-mono-nerd-font/releases/download/v3.4.0/dm-mono-nerd-font-3.4.0.tar.gz"
  sha256 "f47243c7716570ee33a049b6562ddf5603056105607ceef92f742b0bb7e35062"

  def install
    system "tar", "-xzf", cached_download, "--strip-components=1", "-C", prefix
  end

  def caveats
    <<~EOS
      Fonts are installed to #{prefix}.
      To make them available system-wide, copy to ~/Library/Fonts:
        cp #{prefix}/*.ttf ~/Library/Fonts/
    EOS
  end

  test do
  end
end